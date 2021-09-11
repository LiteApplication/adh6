from sqlalchemy.engine.create import create_engine
from src.constants import MembershipDuration, MembershipStatus
import uuid
from datetime import date, datetime, timedelta
from typing import Dict, List, Optional
from sqlalchemy.orm import Session
from common import init
from flask_script import Manager
from flask_migrate import MigrateCommand
from faker import Faker

import ipaddress
from src.interface_adapter.sql.model.database import Database
from src.interface_adapter.sql.model.models import Adherent, AccountType, Adhesion, Membership, Modification, PaymentMethod, Routeur, Transaction, Vlan, Switch, Port, Chambre, Admin, Caisse, Account, Device, Product
application, migrate = init(testing=False, managing=True)

manager = Manager(application.app)
manager.add_command('db', MigrateCommand)

@manager.command
def check_subnet():
    public_range = ipaddress.IPv4Network("157.159.192.0/22").address_exclude(ipaddress.IPv4Network("157.159.195.0/24"))
    excluded_addresses = ["157.159.192.0", "157.159.192.1", "157.159.192.255", "157.159.193.0", "157.159.193.1", "157.159.193.255", "157.159.194.0", "157.159.194.1", "157.159.194.255"]
    hosts = []
    for r in public_range:
        hosts.extend(list(r.hosts()))
    private_range = ipaddress.IPv4Network("10.42.0.0/16").subnets(new_prefix=28)
    mappings = {}
    for subnet, ip in zip(private_range, hosts):
        if str(ip) in excluded_addresses:
            continue
        mappings[str(subnet)] = str(ip)

    s: Session = Database.get_db().get_session()
    adherents: List[Adherent] = s.query(Adherent).all()
    i = 1
    for a in adherents:
        if a.date_de_depart is None:
            # print(f'{a.login}: Has no departure date')
            continue
        if a.ip is None or a.subnet is None:
            continue
        if a.date_de_depart < date.today() and a.subnet is not None and a.subnet != "":
            print(f'{a.login}: Should not have any subnet')
            continue
        if a.ip is None:
            continue
        if a.subnet not in mappings:
            print(f'{a.login}: {a.ip} is not in the mapping')
            continue
        if a.ip != mappings[a.subnet]:
            i += 1
            print(f'{a.login}: {a.subnet} is not in mapped to {a.ip} but to {mappings[a.subnet]}')
    print(i)

limit_departure_date = date(2019, 1, 1)
@manager.command
def remove_members():
    s: Session = Database.get_db().get_session()
    adherents: List[Adherent] = s.query(Adherent).filter(Adherent.date_de_depart <= limit_departure_date).all()

    passed_adherents: List[Adherent] = []
    total = len(adherents)
    total_lines = 0
    deleted_devices = 0
    deleted_modifications = 0
    for i, a in enumerate(adherents):
        print(f'{i}/{total}: {a.login}, {a.created_at}')
        accounts: List[Account] = s.query(Account).filter(Account.adherent_id == a.id).all()
        pass_adherent = False
        for acc in accounts:
            transactions: List[Transaction] = s.query(Transaction).filter(Transaction.src == acc.id).all()
            transactions_from: List[Transaction] = s.query(Transaction).filter(Transaction.author_id == a.id).all()
            if len(transactions) != 0 or len(transactions_from) != 0:
                print("Adherent passed")
                passed_adherents.append(a)
                pass_adherent = True
                continue
            s.delete(acc)
            total_lines += 1
        if pass_adherent:
            continue
        devices: List[Device] = s.query(Device).filter(Device.adherent_id == a.id).all()
        for d in devices:
            s.delete(d)
            total_lines += 1
            deleted_devices += 1
        adhesions: List[Adhesion] = s.query(Adhesion).filter(Adhesion.adherent_id == a.id).all()
        for add in adhesions:
            s.delete(add)
            total_lines += 1
        routeurs: List[Routeur] = s.query(Routeur).filter(Routeur.adherent_id == a.id).all()
        for r in routeurs:
            s.delete(r)
            total_lines += 1
        modifications: List[Modification] = s.query(Modification).filter(Modification.adherent_id == a.id).all()
        for m in modifications:
            s.delete(m)
            total_lines += 1
            deleted_modifications += 1
        s.delete(a)
    print(f'deleted lines: {total_lines}, ')
    s.commit()
   
@manager.command
def check_transactions_member_to_remove():
    s: Session = Database.get_db().get_session()
    adherents: List[Adherent] = s.query(Adherent).filter(Adherent.date_de_depart <= limit_departure_date).all()

    total = len(adherents)
    for i, a in enumerate(adherents):
        print(f'{i}/{total}: {a.login}, {a.created_at}')
        devices: List[Device] = s.query(Device).filter(Device.adherent_id == a.id).all()
        for d in devices:
            s.delete(d)
        adhesions: List[Adhesion] = s.query(Adhesion).filter(Adhesion.adherent_id == a.id).all()
        for add in adhesions:
            s.delete(add)
        routeurs: List[Routeur] = s.query(Routeur).filter(Routeur.adherent_id == a.id).all()
        for r in routeurs:
            s.delete(r)
        accounts: List[Account] = s.query(Account).filter(Account.adherent_id == a.id).all()
        for acc in accounts:
            print(acc.id)
            transactions: List[Transaction] = s.query(Transaction).filter(Transaction.src == acc.id).all() + s.query(Transaction).filter(Transaction.author_id == a.id).all()
            for t in transactions:
                print(a.id)
                print(t.name)
    s.commit() 

@manager.command
def generate_membership():
    s: Session = Database.get_db().get_session()
    adherents: List[Adherent] = s.query(Adherent).filter(Adherent.date_de_depart >= limit_departure_date).all()
    products: Dict[str, Product] = {}
    products_sql = s.query(Product).all()
    for p in products_sql:
        products[p.name] = p

    for adherent in adherents:
        print(adherent.login)
        memberships: List[Membership] = s.query(Membership).filter(Membership.adherent_id == adherent.id).all()
        if memberships != []:
            print("Already have a membership")
            continue
        membership: Membership = Membership(
            uuid=str(uuid.uuid4()),
            account_id=None,
            create_at=adherent.created_at,
            has_room=False,
            duration=MembershipDuration.NONE,
            first_time=False,
            adherent_id=adherent.id,
            payment_method_id=None,
            products="",
            status=MembershipStatus.COMPLETE,
            update_at=adherent.created_at,

        )
        account = s.query(Account).filter(Account.adherent_id == adherent.id).one_or_none()
        if account is None:
            print("No Account")
            s.add(membership)
            continue
        membership.account_id = account.id
        transactions: List[Transaction] = s.query(Transaction).filter(Transaction.src == account.id).all()
        if not transactions:
            print("Empty Account")
            s.add(membership)
            continue
        grouped_transactions: Dict[date, List[Transaction]] = {}
        first_date: Optional[date] = None
        for transaction in transactions:
            if first_date is None or first_date > transaction.timestamp.date():
                first_date = transaction.timestamp.date()
            if transaction.timestamp.date() not in grouped_transactions:
                grouped_transactions[transaction.timestamp.date()] = [transaction]
            else:
                grouped_transactions[transaction.timestamp.date()].append(transaction)

        for d, ts in grouped_transactions.items():
            print(d)
            current_products: List[int] = []
            membership: Membership = Membership(
                uuid=str(uuid.uuid4()),
                account_id=account.id,
                create_at=adherent.created_at,
                has_room=False,
                duration=MembershipDuration.NONE,
                first_time=False,
                adherent_id=adherent.id,
                payment_method_id=None,
                products="",
                status=MembershipStatus.COMPLETE,
                update_at=adherent.created_at,
            )
            for t in ts:
                if membership.duration == MembershipDuration.NONE:
                    membership.create_at = t.timestamp
                    membership.update_at = t.timestamp
                    membership.first_time = t.timestamp.date() == first_date
                    if t.name.startswith('Internet'):
                        membership.has_room = True
                        membership.create_at = t.timestamp
                        membership.update_at = t.timestamp
                        membership.first_time = t.timestamp.date() == first_date
                        if t.name.endswith('1 mois'):
                            membership.duration = MembershipDuration.ONE_MONTH
                        if t.name.endswith('2 mois'):
                            membership.duration = MembershipDuration.TWO_MONTH
                        if t.name.endswith('3 mois'):
                            membership.duration = MembershipDuration.THREE_MONTH
                        if t.name.endswith('4 mois'):
                            membership.duration = MembershipDuration.FOUR_MONTH
                        if t.name.endswith('5 mois'):
                            membership.duration = MembershipDuration.FIVE_MONTH
                        if t.name.endswith('6 mois'):
                            membership.duration = MembershipDuration.SIX_MONTH
                        if t.name.endswith('1 an'):
                            membership.duration = MembershipDuration.ONE_YEAR
                        if t.name.endswith('sans chambre'):
                            membership.has_room = False
                            membership.duration = MembershipDuration.ONE_YEAR
                        print(membership.duration)
                if t.name in products:
                    current_products.append(products[t.name].id)
            membership.products = str(current_products) if current_products != [] else ""
            s.add(membership)
    s.commit()

@manager.command
def todays_subscriptions():
    s: Session = Database.get_db().get_session()
    now = datetime.now()
    today = datetime(now.year, now.month, now.day)
    tomorrow = today + timedelta(1)
    print(today)
    print(tomorrow)
    adherents: List[Adherent] = s.query(Adherent).filter(Adherent.date_de_depart >= limit_departure_date).filter(Adherent.updated_at <= tomorrow, Adherent.updated_at >= today).all()
    with open("memberships.md", "w+") as f:
        f.writelines(["|#|Login|Create At|Update At|Account Name|First time|Duration|Transaction Name|Transaction Timestamp|\n", "|-|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n"])
        for i, adherent in enumerate(adherents):
            print(adherent.login)
            account: Account = s.query(Account).filter(Account.adherent_id == adherent.id).one_or_none()
            if account is None:
                f.writelines(f'|{i}|{adherent.login}|{adherent.created_at}|{adherent.updated_at}|None|None|None|None|None|\n')
                continue
            memberships: List[Membership] = s.query(Membership).filter(Membership.adherent_id == adherent.id).all()
            if not memberships:
                print("no membership")
                continue
            for m in memberships:
                create_at = datetime(m.create_at.year, m.create_at.month, m.create_at.day)
                transactions: List[Transaction] = s.query(Transaction).filter(Transaction.src == account.id, Transaction.timestamp >= create_at, Transaction.timestamp <= create_at + timedelta(1)).order_by(Transaction.timestamp.asc()).all()
                if not transactions:
                    print(f"no transaction for membership {m.uuid}")
                    continue
                for j, t in enumerate(transactions):
                    if j == 0:
                        f.writelines(f'|{i}|{adherent.login}|{adherent.created_at}|{adherent.updated_at}|{account.name}|{m.first_time}|{m.duration}|{t.name}|{t.timestamp}|\n')
                    else:
                        f.writelines(f'||||||||{t.name}|{t.timestamp}|\n')

@manager.command
def reset_membership():
    s: Session = Database.get_db().get_session()
    memberships: List[Membership] = s.query(Membership).all()
    for m in memberships:
        print(m.uuid)
        s.delete(m)
    s.commit()

@manager.command
def check_migration_from_adh5():
    engine = create_engine('')
    s: Session = Database.get_db().get_session()
    i = 0
    j = 0
    total = 0
    adherents: List[Adherent] = s.query(Adherent).filter(Adherent.date_de_depart >= limit_departure_date).all()
    with open("migration_transactions.md", "w+") as f:
        f.writelines(["# Missing Transactions\n"])
        for adherent in adherents:
            # Check an account exist, if not create a fake one (for now)
            account: Account = s.query(Account).filter(Account.adherent_id == adherent.id).one_or_none()
            if account is None:
                print("Creation of an account")
                account = Account(
                    type=2,
                    creation_date=adherent.created_at,
                    name=f'{adherent.prenom} {adherent.nom.upper()} ({adherent.login})',
                    actif=True,
                    compte_courant=False,
                    pinned=False,
                    adherent_id=adherent.id
                )
                s.add(account)
                s.flush()
            
            transactions: List[Transaction] = s.query(Transaction).filter(Transaction.src == account.id).all()
            adh5_transactions: List[Transaction] = []
            with engine.connect() as connection:
                adh5_adherents = connection.execute("SELECT id FROM adherents WHERE login='{}'".format(adherent.login))
                adh5_adherent_id = 0
                for row in adh5_adherents:
                    adh5_adherent_id = row['id']
                
                ecritures = connection.execute("SELECT * FROM ecritures WHERE adherent_id={} AND created_at >= '{}'".format(adh5_adherent_id, datetime(2020, 2, 15)))
                for e in ecritures:
                    adh5_transactions.append(Transaction(
                        value=e['montant'],
                        timestamp=e['date'],
                        src=account.id,
                        dst=1,
                        name=e['intitule'],
                        attachments="",
                        type=e['moyen'],
                        author_id=adherent.id,
                        pending_validation=False
                    ))
            if len(adh5_transactions) == 0:
                continue
            missing_transactions: List[Transaction] = []
            for adh5_t in adh5_transactions:
                if len(transactions) == 0:
                    missing_transactions.append(adh5_t)
                    continue
                in_adh6 = False
                for t in transactions:
                    if adh5_t.name == t.name and adh5_t.timestamp.date() == t.timestamp.date():
                        in_adh6 = True
                        break
                if not in_adh6:
                    missing_transactions.append(adh5_t)
            j += len(missing_transactions)
            if len(missing_transactions) == 0:
                continue
            f.writelines([f"## {adherent.login}\n", "|*Name*|*Timestamp*|*Value*|\n", "|:-:|:-:|:-:|\n"])
            sum_adh = 0
            print(adherent.login)
            for t in missing_transactions:
                total += t.value
                print("{}, {}, {}".format(t.name, t.timestamp, t.value))
                f.write("|{}|{}|{}|\n".format(t.name, t.timestamp, t.value))
                sum_adh += t.value
            f.write("|||*{}*|\n".format(sum_adh))
            i += 1
        print(f'{i} adherent, {j} transactions, {total} €')


@manager.command
def seed():
    """Add seed data to the database."""
    s = Database.get_db().get_session()

    print("Seeding account types")
    account_types = [1,"Special"],[2,"Adherent"],[3,"Club interne"],[4,"Club externe"],[5,"Association externe"]
    for type in account_types:
        s.add(
            AccountType(
                id=type[0],
                name=type[1]
            )
        )

    print("Seeding MiNET accounts")
    accounts = [1, 1, "MiNET frais techniques", True, None, True, True],[2, 1, "MiNET frais asso", True, None, True, True]
    for account in accounts:
        s.add(
            Account(
                id=account[0],
                type=account[1],
                name=account[2],
                actif=account[3],
                adherent_id=account[4],
                compte_courant=account[5],
                pinned=account[6]
            )
        )

    print("Seeding Products")
    products = [1,"Cable 3m", 3, 3],[2,"Cable 5m", 5, 5],[3,"Adaptateur USB/Ethernet", 13.00, 13.00],[4,"Adaptateur USB-C/Ethernet", 12.00, 12.00]
    for product in products:
        s.add(
            Product(
                id=product[0],
                name=product[1],
                buying_price=product[2],
                selling_price=product[3]
            )
        )

    print("Seeding payment methods")
    payment_methods = [1,"Liquide"],[2,"Chèque"],[3,"Carte bancaire"],[4,"Virement"],[5,"Stripe"]
    for method in payment_methods:
        s.add(
            PaymentMethod(
                id=method[0],
                name=method[1]
            )
        )

    print("Seeding cashbox")
    s.add(Caisse(
        fond=0,
        coffre=0
    ))

    print("Seeding vlans")
    s.bulk_save_objects([
        Vlan(
            numero=35,
            adresses="10.42.0.0/16",
            adressesv6="",
            excluded_addr="",
            excluded_addrv6="",
        ),
        Vlan(
            numero=36,
            adresses="157.159.192.0/22",
            adressesv6="",
            excluded_addr="157.159.195.0/24",
            excluded_addrv6="",
        ),
        Vlan(
            numero=30,
            adresses="172.30.0.0/16",
            adressesv6="",
            excluded_addr="",
            excluded_addrv6="",
        ),
        Vlan(
            numero=41,
            adresses="157.159.41.0/24",
            adressesv6="",
            excluded_addr="157.159.41.1/32",
            excluded_addrv6="",
        )
    ])

    s.commit()


@manager.option('-l', '--login', help='Your login', default='dummy_user')
@manager.command
def fake(login):
    """Add dummy data to the database."""
    fake = Faker()
    s = Database.get_db().get_session()
    #switch = Switch(
    #    description="Dummy switch",
    #    ip="192.168.254.254",
    #    communaute="adh6",
    #)
    #s.add(switch)

    switch2 = Switch(
        description="Switch local",
        ip="192.168.102.219",
        communaute="adh5",
    )
    s.add(switch2)

    chambres = []
    for n in range(1, 30):
        chambre = Chambre(
            numero=n,
            description="Chambre " + str(n),
            vlan_id=3
        )
        chambres.append(chambre)
        s.add(chambre)

    #for n in range(1, 10):
    #    s.add(Port(
    #        rcom=0,
    #        numero="1/0/" + str(n),
    #        oid="1010" + str(n),
    #        switch=switch,
    #        chambre=chambres[n - 1]
    #    ))

    for n in range(1, 10):
        s.add(Port(
            rcom=0,
            numero="1/0/" + str(n),
            oid="1010" + str(n),
            switch=switch2,
            chambre=chambres[n-1]
        ))


    for n in range(10, 20):
        s.add(Port(
            rcom=0,
            numero="1/0/" + str(n),
            oid="101" + str(n),
            switch=switch2,
            chambre=chambres[n-1]
        ))


    admin = Admin(
        roles="adh6_user,adh6_admin,adh6_treso,adh6_superadmin"
    )
    s.add(admin)

    adherent = Adherent(
        nom=fake.last_name_nonbinary(),
        prenom=fake.first_name_nonbinary(),
        mail=fake.email(),
        login=login,
        password="",
        chambre=chambres[2],
        admin=admin
    )
    s.add(adherent)
    s.add(
        Account(
            type=1,
            name=adherent.nom + " " + adherent.prenom,
            actif=True,
            compte_courant=True,
            pinned=False,
            adherent=adherent
        )
    )

    for n in range(1, 4):
        s.add(Device(
            mac=fake.mac_address(),
            ip=None,
            adherent=adherent,
            ipv6=None,
            type=0
        ))
    for n in range(1, 4):
        s.add(Device(
            mac=fake.mac_address(),
            ip=None,
            adherent=adherent,
            ipv6=None,
            type=1
        ))
    s.commit()



if __name__ == '__main__':
    manager.run()
