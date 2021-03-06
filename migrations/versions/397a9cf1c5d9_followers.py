"""followers

Revision ID: 397a9cf1c5d9
Revises: 8e9c042c9dc5
Create Date: 2019-05-29 19:30:17.796842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '397a9cf1c5d9'
down_revision = '8e9c042c9dc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
