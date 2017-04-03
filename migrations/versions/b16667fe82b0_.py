"""empty message

Revision ID: b16667fe82b0
Revises: 4b2424d9f6a6
Create Date: 2017-04-02 22:53:39.166341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b16667fe82b0'
down_revision = '4b2424d9f6a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session_levels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Text(length=128), nullable=True),
    sa.Column('phone_number', sa.String(length=25), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('session_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone_number', sa.String(length=64), nullable=False),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('account', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_phone_number'), 'users', ['phone_number'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_phone_number'), table_name='users')
    op.drop_table('users')
    op.drop_table('session_levels')
    # ### end Alembic commands ###
