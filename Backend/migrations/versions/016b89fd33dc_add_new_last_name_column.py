"""add new last_name column

Revision ID: 016b89fd33dc
Revises: 2365de670392
Create Date: 2021-03-24 18:28:00.213016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '016b89fd33dc'
down_revision = '2365de670392'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_name', sa.String(length=50), nullable=False))
    op.alter_column('user', 'first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_column('user', 'last_name')
    # ### end Alembic commands ###
