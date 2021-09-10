"""empty message

Revision ID: a46ac86f2607
Revises: 401eda918023
Create Date: 2021-09-11 00:03:51.457013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a46ac86f2607'
down_revision = '401eda918023'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('is_archive', sa.Boolean(), nullable=True))
    op.add_column('transactions', sa.Column('membership_uuid', sa.CHAR(length=36), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transactions', 'membership_uuid')
    op.drop_column('transactions', 'is_archive')
    # ### end Alembic commands ###
