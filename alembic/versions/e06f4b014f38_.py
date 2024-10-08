"""empty message

Revision ID: e06f4b014f38
Revises: 4bfbea5c64bf
Create Date: 2024-09-11 19:27:41.762644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e06f4b014f38'
down_revision: Union[str, None] = '4bfbea5c64bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('to_do_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('to_do_list')
    # ### end Alembic commands ###
