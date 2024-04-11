"""empty message

Revision ID: 3a84d9c0de03
Revises: 07b6875f0fdf
Create Date: 2024-04-04 21:58:30.794914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a84d9c0de03'
down_revision: Union[str, None] = '07b6875f0fdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('film', 'film_id',
               existing_type=sa.INTEGER(),
               type_=sa.Text(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('film', 'film_id',
               existing_type=sa.Text(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###