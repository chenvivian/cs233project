"""empty message

Revision ID: 77b81f1e28d3
Revises: 78cbcc691677
Create Date: 2019-03-22 17:49:58.315878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77b81f1e28d3'
down_revision = '78cbcc691677'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'posted')
    # ### end Alembic commands ###
