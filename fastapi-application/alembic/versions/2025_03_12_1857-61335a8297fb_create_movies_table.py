"""create movies table

Revision ID: 61335a8297fb
Revises:
Create Date: 2025-03-12 18:57:05.211792

"""

from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "61335a8297fb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "movie",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("release_date", sa.Date(), nullable=False),
        sa.Column("release_date_cinero", sa.Date(), nullable=False),
        sa.Column("maturity_rating", sa.String(length=10), nullable=False),
        sa.Column("duration", sa.Integer(), nullable=False),
        sa.Column("video_quality", sa.String(length=30), nullable=False),
        sa.Column("audio_quality", sa.String(length=30), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("is_free", sa.Boolean(), nullable=False),
        sa.Column("in_slider", sa.Boolean(), nullable=False),
        sa.Column("renting_period", sa.Integer(), nullable=False),
        sa.Column("vod", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_movie")),
        sa.UniqueConstraint("name", name=op.f("uq_movie_name")),
        sa.UniqueConstraint("slug", name=op.f("uq_movie_slug")),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_user")),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_table(
        "access_token",
        sa.Column("token", sa.String(length=43), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name=op.f("fk_access_token_user_id_user"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("token", name=op.f("pk_access_token")),
    )
    op.create_index(
        op.f("ix_access_token_created_at"),
        "access_token",
        ["created_at"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_access_token_created_at"), table_name="access_token")
    op.drop_table("access_token")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_table("movie")
    # ### end Alembic commands ###
