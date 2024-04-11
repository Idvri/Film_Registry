"""empty message

Revision ID: c67ca26edad4
Revises: de65325ef58a
Create Date: 2024-04-04 19:49:32.771460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c67ca26edad4'
down_revision: Union[str, None] = 'de65325ef58a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('film', 'start_date',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('film', 'start_date',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###
