"""empty message

Revision ID: 274fe4e4c4d2
Revises:
Create Date: 2018-06-26 11:33:30.017433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '274fe4e4c4d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Admin',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('photoURL', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Reset Password Token',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('photoURL', sa.String(), nullable=True),
    sa.Column('allowed_usage', sa.Integer(), nullable=True),
    sa.Column('ftl', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('siteAdmin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Utilities',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('pricing', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Badges',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('csv', sa.String(length=100), nullable=False),
    sa.Column('text_color', sa.String(length=100), nullable=False),
    sa.Column('badge_size', sa.String(length=100), nullable=False),
    sa.Column('download_link', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('File',
    sa.Column('id', sa.String(length=100), nullable=True),
    sa.Column('filename', sa.String(length=100), nullable=False),
    sa.Column('filetype', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('filename')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('File')
    op.drop_table('Badges')
    op.drop_table('Utilities')
    op.drop_table('User')
    op.drop_table('Reset Password Token')
    op.drop_table('Admin')
    # ### end Alembic commands ###
