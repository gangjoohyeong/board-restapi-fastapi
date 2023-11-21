"""empty message

Revision ID: 260aaa366468
Revises: 
Create Date: 2023-11-20 22:24:00.081385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '260aaa366468'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_data', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    # ### end Alembic commands ###