"""empty message

Revision ID: 653e817fc054
Revises: 7b32c8e1ebe4
Create Date: 2023-11-21 21:28:50.219875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '653e817fc054'
down_revision = '7b32c8e1ebe4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    # ### end Alembic commands ###
