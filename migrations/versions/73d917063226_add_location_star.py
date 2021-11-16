"""Add location, star

Revision ID: 73d917063226
Revises: 076c8ab3ffa6
Create Date: 2021-11-16 12:02:16.906250

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '73d917063226'
down_revision = '076c8ab3ffa6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    location_enum = postgresql.ENUM('front', 'back', 'side', name='location_enum')
    location_enum.create(op.get_bind())

    op.add_column('cafes', sa.Column('location', sa.Enum('front', 'back', 'side', name='location_enum'), nullable=True))
    op.add_column('cafes', sa.Column('star', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cafes', 'star')
    op.drop_column('cafes', 'location')

    location_enum = postgresql.ENUM('front', 'back', 'side', name='location_enum')
    location_enum.drop(op.get_bind())
    # ### end Alembic commands ###
