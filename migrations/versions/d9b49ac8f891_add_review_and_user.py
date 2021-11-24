"""Add review and user

Revision ID: d9b49ac8f891
Revises: 73d917063226
Create Date: 2021-11-24 22:47:43.412184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9b49ac8f891'
down_revision = '73d917063226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('kakao_id', sa.String(), nullable=False),
    sa.Column('nickname', sa.String(), nullable=False),
    sa.Column('student_type', sa.String(), nullable=True),
    sa.Column('student_year', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_table('reviews',
    sa.Column('writer_id', sa.String(), nullable=False),
    sa.Column('cafe_id', sa.String(), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=True),
    sa.Column('star', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['cafe_id'], ['cafes.id'], name=op.f('fk_reviews_cafe_id_cafes')),
    sa.ForeignKeyConstraint(['writer_id'], ['users.id'], name=op.f('fk_reviews_writer_id_users')),
    sa.PrimaryKeyConstraint('writer_id', 'cafe_id', name=op.f('pk_reviews'))
    )
    op.add_column('cafes', sa.Column('created_by_id', sa.String(), nullable=True))
    op.create_foreign_key(op.f('fk_cafes_created_by_id_users'), 'cafes', 'users', ['created_by_id'], ['id'])
    op.drop_column('cafes', 'created_by')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cafes', sa.Column('created_by', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(op.f('fk_cafes_created_by_id_users'), 'cafes', type_='foreignkey')
    op.drop_column('cafes', 'created_by_id')
    op.drop_table('reviews')
    op.drop_table('users')
    # ### end Alembic commands ###
