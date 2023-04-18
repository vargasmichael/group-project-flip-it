"""players.id

Revision ID: cd3e5ab24588
Revises: 46c9a2ce5207
Create Date: 2023-04-18 10:25:42.611598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd3e5ab24588'
down_revision = '46c9a2ce5207'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.add_column(sa.Column('player_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_cards_card_id_cards', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_cards_player_id_players'), 'players', ['player_id'], ['id'])
        batch_op.drop_column('card_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.add_column(sa.Column('card_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_cards_player_id_players'), type_='foreignkey')
        batch_op.create_foreign_key('fk_cards_card_id_cards', 'cards', ['card_id'], ['id'])
        batch_op.drop_column('player_id')

    # ### end Alembic commands ###
