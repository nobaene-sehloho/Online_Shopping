"""Added the confirmed and confirmed_on columns.

Revision ID: f156efcd0751
Revises: 8389719e9d9f
Create Date: 2021-03-25 17:15:47.066845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f156efcd0751'
down_revision = '8389719e9d9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('confirmed_on', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed_on')
    op.drop_column('user', 'confirmed')
    # ### end Alembic commands ###
