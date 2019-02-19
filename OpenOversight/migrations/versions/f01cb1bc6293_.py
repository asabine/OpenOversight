"""empty message

Revision ID: f01cb1bc6293
Revises: 2a9064a2507c
Create Date: 2019-02-19 15:41:49.010897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f01cb1bc6293'
down_revision = '2a9064a2507c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('officers', sa.Column('last_employment_date', sa.String(length=50), nullable=True))
    op.add_column('officers', sa.Column('last_employment_details', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('officers', 'last_employment_details')
    op.drop_column('officers', 'last_employment_date')
    # ### end Alembic commands ###
