"""deleted confirmed.

Revision ID: e6042ccceef1
Revises: 7a914bb8365a
Create Date: 2021-03-25 21:24:29.360898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6042ccceef1'
down_revision = '7a914bb8365a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed')
    op.drop_column('user', 'confirmed_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed_on', sa.DATETIME(), nullable=True))
    op.add_column('user', sa.Column('confirmed', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###