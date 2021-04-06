"""Added brand and category models.

Revision ID: abb1e4185700
Revises: 9149842fd08d
Create Date: 2021-04-01 23:07:00.750774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abb1e4185700'
down_revision = '9149842fd08d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('brand', sa.Column('brand_name', sa.String(length=30), nullable=False))
    op.create_unique_constraint(None, 'brand', ['brand_name'])
    op.drop_column('brand', 'name')
    op.add_column('category', sa.Column('category_name', sa.String(length=30), nullable=False))
    op.create_unique_constraint(None, 'category', ['category_name'])
    op.drop_column('category', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('name', sa.VARCHAR(length=30), nullable=False))
    op.drop_constraint(None, 'category', type_='unique')
    op.drop_column('category', 'category_name')
    op.add_column('brand', sa.Column('name', sa.VARCHAR(length=30), nullable=False))
    op.drop_constraint(None, 'brand', type_='unique')
    op.drop_column('brand', 'brand_name')
    # ### end Alembic commands ###