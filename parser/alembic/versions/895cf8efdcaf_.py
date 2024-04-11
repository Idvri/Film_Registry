"""empty message

Revision ID: 895cf8efdcaf
Revises: 9f1496f423e3
Create Date: 2024-04-04 22:06:57.434288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '895cf8efdcaf'
down_revision: Union[str, None] = '9f1496f423e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('film', 'date_of_registration',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('film', 'date_of_registration',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###