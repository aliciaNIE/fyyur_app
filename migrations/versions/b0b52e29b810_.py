"""empty message

Revision ID: b0b52e29b810
Revises: 641732c6a8e1
Create Date: 2022-06-26 14:56:41.156284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0b52e29b810'
down_revision = '641732c6a8e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Show', 'start_time',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Show', 'start_time',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
