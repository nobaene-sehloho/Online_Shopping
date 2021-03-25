"""Added the confirmed and confirmed_on columns.

Revision ID: fb8d34afc3b2
Revises: 6bc3da1f3583
Create Date: 2021-03-25 17:33:23.072463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb8d34afc3b2'
down_revision = '6bc3da1f3583'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed_on')
    # ### end Alembic commands ###