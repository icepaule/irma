"""DB revision creation

Revision ID: 2cc69d5c53eb
Revises:
Create Date: 2015-05-20 13:54:25.433439

"""

# revision identifiers, used by Alembic.
revision = '2cc69d5c53eb'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('irma_file',
                    sa.Column('id',
                              sa.Integer(),
                              nullable=False),
                    sa.Column('sha256',
                              sa.String(length=64),
                              nullable=True),
                    sa.Column('sha1',
                              sa.String(length=40),
                              nullable=True),
                    sa.Column('md5',
                              sa.String(length=32),
                              nullable=True),
                    sa.Column('timestamp_first_scan',
                              sa.Float(precision=2),
                              nullable=False),
                    sa.Column('timestamp_last_scan',
                              sa.Float(precision=2),
                              nullable=False),
                    sa.Column('size',
                              sa.Integer(),
                              nullable=True),
                    sa.Column('path',
                              sa.String(length=255),
                              nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sqlite_autoincrement=True
                    )
    op.create_index(op.f('ix_irma_file_md5'),
                    'irma_file', ['md5'],
                    unique=False)
    op.create_index(op.f('ix_irma_file_sha1'),
                    'irma_file', ['sha1'],
                    unique=False)
    op.create_index(op.f('ix_irma_file_sha256'),
                    'irma_file', ['sha256'],
                    unique=False)
    op.create_table('irma_scan',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('external_id', sa.String(length=36),
                              nullable=False),
                    sa.Column('date', sa.Integer(), nullable=False),
                    sa.Column('ip', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sqlite_autoincrement=True
                    )
    op.create_index(op.f('ix_irma_scan_external_id'),
                    'irma_scan',
                    ['external_id'],
                    unique=False)
    op.create_table('irma_submission',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('external_id', sa.String(length=36),
                              nullable=False),
                    sa.Column('os_name', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('ip', sa.String(), nullable=False),
                    sa.Column('date', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sqlite_autoincrement=True
                    )
    op.create_index(op.f('ix_irma_submission_external_id'),
                    'irma_submission',
                    ['external_id'],
                    unique=False)
    op.create_table('irma_tag',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sqlite_autoincrement=True
                    )
    op.create_table('irma_fileAgent',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('submission_path',
                              sa.String(length=255),
                              nullable=False),
                    sa.Column('id_file', sa.Integer(), nullable=False),
                    sa.Column('id_s', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['id_file'], ['irma_file.id'], ),
                    sa.ForeignKeyConstraint(['id_s'],
                                            ['irma_submission.id'],),
                    sa.PrimaryKeyConstraint('id'),
                    sqlite_autoincrement=True
                    )
    op.create_table('irma_fileWeb',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('scan_file_idx', sa.Integer(), nullable=False),
                    sa.Column('id_file', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('id_scan', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['id_file'], ['irma_file.id'], ),
                    sa.ForeignKeyConstraint(['id_scan'], ['irma_scan.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id_scan', 'scan_file_idx')
                    )
    op.create_table('irma_probeResult',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('type', sa.String(), nullable=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('nosql_id', sa.String(), nullable=True),
                    sa.Column('status', sa.Integer(), nullable=True),
                    sa.Column('id_file', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['id_file'], ['irma_file.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sqlite_autoincrement=True
                    )
    op.create_table('irma_scanEvents',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('status', sa.Integer(), nullable=False),
                    sa.Column('timestamp', sa.Float(precision=2),
                              nullable=False),
                    sa.Column('id_scan', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['id_scan'], ['irma_scan.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sqlite_autoincrement=True
                    )
    op.create_index(op.f('ix_irma_scanEvents_id_scan'),
                    'irma_scanEvents',
                    ['id_scan'], unique=False)
    op.create_table('irma_tag_file',
                    sa.Column('id_tag', sa.Integer(), nullable=True),
                    sa.Column('id_file', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['id_file'], ['irma_file.id'], ),
                    sa.ForeignKeyConstraint(['id_tag'], ['irma_tag.id'], )
                    )
    op.create_table('irma_probeResult_fileWeb',
                    sa.Column('id_fw', sa.Integer(), nullable=True),
                    sa.Column('id_pr', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['id_fw'], ['irma_fileWeb.id'], ),
                    sa.ForeignKeyConstraint(['id_pr'],
                                            ['irma_probeResult.id'],)
                    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('irma_probeResult_fileWeb')
    op.drop_table('irma_tag_file')
    op.drop_index(op.f('ix_irma_scanEvents_id_scan'),
                  table_name='irma_scanEvents')
    op.drop_table('irma_scanEvents')
    op.drop_table('irma_probeResult')
    op.drop_table('irma_fileWeb')
    op.drop_table('irma_fileAgent')
    op.drop_table('irma_tag')
    op.drop_index(op.f('ix_irma_submission_external_id'),
                  table_name='irma_submission')
    op.drop_table('irma_submission')
    op.drop_index(op.f('ix_irma_scan_external_id'),
                  table_name='irma_scan')
    op.drop_table('irma_scan')
    op.drop_index(op.f('ix_irma_file_sha256'),
                  table_name='irma_file')
    op.drop_index(op.f('ix_irma_file_sha1'),
                  table_name='irma_file')
    op.drop_index(op.f('ix_irma_file_md5'),
                  table_name='irma_file')
    op.drop_table('irma_file')
    ### end Alembic commands ###
