"""empty message

Revision ID: a9907f698183
Revises: c99a3d66516b
Create Date: 2021-01-31 12:50:22.323963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9907f698183'
down_revision = 'c99a3d66516b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('password', sa.String(length=128), nullable=True))
    op.add_column('admin', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'admin', ['username'])
    op.drop_constraint('contact_admin_id_fkey', 'contact', type_='foreignkey')
    op.drop_column('contact', 'admin_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('admin_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('contact_admin_id_fkey', 'contact', 'admin', ['admin_id'], ['id'])
    op.drop_constraint(None, 'admin', type_='unique')
    op.drop_column('admin', 'username')
    op.drop_column('admin', 'password')
    # ### end Alembic commands ###
