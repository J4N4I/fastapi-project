"""add content column to posts table

Revision ID: 55ad7d12c99e
Revises: 8c7f84b33919
Create Date: 2024-09-17 19:13:42.267602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55ad7d12c99e'
down_revision: Union[str, None] = '8c7f84b33919'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
