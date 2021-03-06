"""Added the confirmed and confirmed_on columns.

Revision ID: 6bc3da1f3583
Revises: f156efcd0751
Create Date: 2021-03-25 17:20:39.380296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bc3da1f3583'
down_revision = 'f156efcd0751'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed_on', sa.DateTime(), nullable=False))
    op.alter_column('user', 'confirmed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'confirmed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_column('user', 'confirmed_on')
    # ### end Alembic commands ###
