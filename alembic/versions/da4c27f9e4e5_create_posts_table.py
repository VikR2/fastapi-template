"""create posts table

Revision ID: da4c27f9e4e5
Revises: 
Create Date: 2022-03-19 13:48:16.799886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da4c27f9e4e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts1',sa.Column('id', sa.Integer(), nullable=False, primary_key=True)),
    sa.Column('title', sa.String(), nullable=False)


def downgrade():
    op.drop_table('posts1')
