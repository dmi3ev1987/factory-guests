"""Initial.

Revision ID: 5a8088bfbf07
Revises: 
Create Date: 2025-04-11 14:27:04.447924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a8088bfbf07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guest_full_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('surname', sa.String(length=128), nullable=False),
    sa.Column('patronymic', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inviter_full_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('surname', sa.String(length=128), nullable=False),
    sa.Column('patronymic', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('place_to_visit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('place', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pass_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guest_full_name_id', sa.Integer(), nullable=True),
    sa.Column('company_name_id', sa.Integer(), nullable=True),
    sa.Column('inviter_full_name_id', sa.Integer(), nullable=True),
    sa.Column('place_to_visit_id', sa.Integer(), nullable=True),
    sa.Column('time_start', sa.DateTime(), nullable=False),
    sa.Column('time_end', sa.DateTime(), nullable=False),
    sa.Column('purpose', sa.Text(), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['company_name_id'], ['company_name.id'], ),
    sa.ForeignKeyConstraint(['guest_full_name_id'], ['guest_full_name.id'], ),
    sa.ForeignKeyConstraint(['inviter_full_name_id'], ['inviter_full_name.id'], ),
    sa.ForeignKeyConstraint(['place_to_visit_id'], ['place_to_visit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pass_request')
    op.drop_table('place_to_visit')
    op.drop_table('inviter_full_name')
    op.drop_table('guest_full_name')
    op.drop_table('company_name')
    # ### end Alembic commands ###
