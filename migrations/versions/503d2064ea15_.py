"""empty message

Revision ID: 503d2064ea15
Revises: 
Create Date: 2017-03-26 14:30:41.199873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '503d2064ea15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_phone_number'), 'users', ['phone_number'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_phone_number'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###