"""empty message

Revision ID: 4d45ccc4e1eb
Revises: ae0ea407f187
Create Date: 2020-02-16 02:41:19.606631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d45ccc4e1eb'
down_revision = 'ae0ea407f187'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('compte_courant', sa.Boolean(), nullable=False))
    op.add_column('accounts', sa.Column('pinned', sa.Boolean(), nullable=False))
    op.add_column('transactions', sa.Column('pending_validation', sa.Boolean(), nullable=False))
    op.drop_index('creation_date', table_name='accounts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transactions', 'pending_validation')
    op.create_index('creation_date', 'accounts', ['creation_date'], unique=True)
    op.drop_column('accounts', 'pinned')
    op.drop_column('accounts', 'compte_courant')
    # ### end Alembic commands ###
