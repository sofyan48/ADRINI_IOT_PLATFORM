CREATE TABLE tb_board (
	id_board INT NOT NULL DEFAULT unique_rowid(),
	nm_board STRING NULL,
	serial_board STRING NULL,
	CONSTRAINT tb_board_pk PRIMARY KEY (id_board ASC),
	FAMILY "primary" (id_board, nm_board, serial_board)
);

CREATE TABLE tb_userdata (
	id_userdata INT NOT NULL DEFAULT unique_rowid(),
	first_name STRING NULL,
	last_name STRING NULL,
	location STRING NULL,
	email STRING NULL,
	CONSTRAINT tb_userdata_pk PRIMARY KEY (id_userdata ASC),
	UNIQUE INDEX tb_userdata_un (email ASC),
	FAMILY "primary" (id_userdata, first_name, last_name, location, email)
);

CREATE TABLE tb_userboard (
	id_userboard INT NOT NULL DEFAULT unique_rowid(),
	id_userdata INT NULL,
	id_board INT NULL,
	CONSTRAINT tb_userboard_pk PRIMARY KEY (id_userboard ASC),
	INDEX tb_userboard_auto_index_tb_userboard_tb_board_fk (id_board ASC),
	INDEX tb_userboard_auto_index_tb_userboard_tb_userdata_fk (id_userdata ASC),
	FAMILY "primary" (id_userboard, id_userdata, id_board)
);

CREATE TABLE tb_channels (
	id_channels INT NOT NULL DEFAULT unique_rowid(),
	id_userboard INT NULL,
	nm_channels STRING NULL,
	channels_key STRING NULL,
	CONSTRAINT tb_channels_pk PRIMARY KEY (id_channels ASC),
	INDEX tb_channels_auto_index_tb_channels_tb_userboard_fk (id_userboard ASC),
	FAMILY "primary" (id_channels, id_userboard, nm_channels, channels_key)
);

CREATE TABLE tb_widget (
	id_widget INT NOT NULL DEFAULT unique_rowid(),
	nm_widget VARCHAR NOT NULL,
	id_channels INT NOT NULL,
	CONSTRAINT newtable_pk PRIMARY KEY (id_widget ASC),
	INDEX newtable_auto_index_newtable_tb_channels_fk (id_channels ASC),
	FAMILY "primary" (id_widget, nm_widget, id_channels)
);

CREATE TABLE tb_moduls (
	id_moduls INT NOT NULL DEFAULT unique_rowid(),
	id_widget INT NOT NULL,
	value_field STRING NOT NULL,
	created_at TIMESTAMPTZ NULL DEFAULT now():::TIMESTAMPTZ,
	CONSTRAINT tb_moduls_pk PRIMARY KEY (id_moduls ASC),
	INDEX tb_moduls_auto_index_tb_moduls_tb_widget_fk (id_widget ASC),
	FAMILY "primary" (id_moduls, id_widget, value_field, created_at)
);

CREATE TABLE tb_user (
	id_user INT NOT NULL DEFAULT unique_rowid(),
	id_userdata INT NULL,
	username STRING NULL,
	password STRING NULL,
	CONSTRAINT tb_user_pk PRIMARY KEY (id_user ASC),
	INDEX tb_user_auto_index_tb_user_tb_userdata_fk (id_userdata ASC),
	UNIQUE INDEX tb_user_username_idx (username ASC),
	FAMILY "primary" (id_user, id_userdata, username, password)
);

CREATE VIEW v_moduls (id_moduls, nm_widget, value_field, id_widget, id_channels, nm_channels, id_userboard, created_at) AS SELECT b1.id_moduls, b2.nm_widget, b1.value_field, b2.id_widget, b3.id_channels, b3.nm_channels, b3.id_userboard, b1.created_at FROM iot_adrini.public.tb_moduls AS b1 JOIN iot_adrini.public.tb_widget AS b2 ON b1.id_widget = b2.id_widget JOIN iot_adrini.public.tb_channels AS b3 ON b2.id_channels = b3.id_channels;

INSERT INTO tb_board (id_board, nm_board, serial_board) VALUES
	(428413380064182273, 'Adrini v1', 'ADR220219-001');

INSERT INTO tb_userdata (id_userdata, first_name, last_name, location, email) VALUES
	(410167896193204225, 'mongkey', 'king', 'alamat', 'meongbego@gmail.com'),
	(428412005040783361, 'adrin', 'thamrin', 'palu', 'adrin@gmail.com');

INSERT INTO tb_userboard (id_userboard, id_userdata, id_board) VALUES
	(428414508716425217, 428412005040783361, 428413380064182273);

INSERT INTO tb_channels (id_channels, id_userboard, nm_channels, channels_key) VALUES
	(428414886846103553, 428414508716425217, 'APLIKASI LAMPU', 'fa4821fc-91dc-43dd-8e73-a578da2f7cc7428414508716425217');

INSERT INTO tb_widget (id_widget, nm_widget, id_channels) VALUES
	(428431221753217025, 'lampu1', 428414886846103553),
	(428431230886084609, 'lampu2', 428414886846103553),
	(428431239601946625, 'lampu3', 428414886846103553),
	(428431248448159745, 'lampu4', 428414886846103553),
	(428431301447745537, 'sensor1', 428414886846103553),
	(428431309607010305, 'sensor2', 428414886846103553),
	(428431317360214017, 'sensor3', 428414886846103553),
	(428431326733631489, 'sensor4', 428414886846103553);

INSERT INTO tb_moduls (id_moduls, id_widget, value_field, created_at) VALUES
	(428434478641709057, 428431301447745537, '0', '2019-02-22 06:50:26.733003+00:00'),
	(428434478694432769, 428431309607010305, '0', '2019-02-22 06:50:26.749151+00:00'),
	(428434478732771329, 428431317360214017, '0', '2019-02-22 06:50:26.760861+00:00'),
	(428434478772158465, 428431326733631489, '0', '2019-02-22 06:50:26.772836+00:00'),
	(428434569070215169, 428431301447745537, '0', '2019-02-22 06:50:54.32962+00:00'),
	(428434569109471233, 428431309607010305, '0', '2019-02-22 06:50:54.341631+00:00'),
	(428434569156132865, 428431317360214017, '0', '2019-02-22 06:50:54.355961+00:00'),
	(428434569199026177, 428431326733631489, '0', '2019-02-22 06:50:54.36801+00:00'),
	(428434569258893313, 428431221753217025, '100', '2019-02-22 06:50:54.387743+00:00'),
	(428434569295265793, 428431230886084609, '200', '2019-02-22 06:50:54.398812+00:00'),
	(428434569339633665, 428431239601946625, '300', '2019-02-22 06:50:54.412281+00:00'),
	(428434569370402817, 428431248448159745, '400', '2019-02-22 06:50:54.421918+00:00'),
	(428434904418975745, 428431301447745537, '1', '2019-02-22 06:52:36.669858+00:00'),
	(428434904460525569, 428431309607010305, '1', '2019-02-22 06:52:36.68261+00:00'),
	(428434904514953217, 428431317360214017, '1', '2019-02-22 06:52:36.699285+00:00'),
	(428434904555945985, 428431326733631489, '1', '2019-02-22 06:52:36.711498+00:00'),
	(428434904595693569, 428431221753217025, '100', '2019-02-22 06:52:36.724132+00:00'),
	(428434904629805057, 428431230886084609, '200', '2019-02-22 06:52:36.734192+00:00'),
	(428434904672665601, 428431239601946625, '300', '2019-02-22 06:52:36.746975+00:00'),
	(428434904706646017, 428431248448159745, '400', '2019-02-22 06:52:36.758053+00:00');

INSERT INTO tb_user (id_user, id_userdata, username, password) VALUES
	(410168663988011009, 410167896193204225, 'mongkey', '$pbkdf2-sha256$29000$9d7b27v3fi.FsHYOgTDmfA$0x00H1i7cthqgyNY/wuNE3A7xd3.Cc.OUaH89td0jTY'),
	(428412694397747201, 428412005040783361, 'adrin', '$pbkdf2-sha256$29000$HaM0BqAUQohRipFSSsm51w$4s0dx/Uplv4SuK7xuU88JDxNfNFevQ7QuX9//NkMRmQ');

ALTER TABLE tb_userboard ADD CONSTRAINT tb_userboard_tb_board_fk FOREIGN KEY (id_board) REFERENCES tb_board (id_board) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tb_userboard ADD CONSTRAINT tb_userboard_tb_userdata_fk FOREIGN KEY (id_userdata) REFERENCES tb_userdata (id_userdata) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tb_channels ADD CONSTRAINT tb_channels_tb_userboard_fk FOREIGN KEY (id_userboard) REFERENCES tb_userboard (id_userboard) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tb_widget ADD CONSTRAINT newtable_tb_channels_fk FOREIGN KEY (id_channels) REFERENCES tb_channels (id_channels) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tb_moduls ADD CONSTRAINT tb_moduls_tb_widget_fk FOREIGN KEY (id_widget) REFERENCES tb_widget (id_widget) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tb_user ADD CONSTRAINT tb_user_tb_userdata_fk FOREIGN KEY (id_userdata) REFERENCES tb_userdata (id_userdata) ON DELETE CASCADE ON UPDATE CASCADE;

-- Validate foreign key constraints. These can fail if there was unvalidated data during the dump.
ALTER TABLE tb_userboard VALIDATE CONSTRAINT tb_userboard_tb_board_fk;
ALTER TABLE tb_userboard VALIDATE CONSTRAINT tb_userboard_tb_userdata_fk;
ALTER TABLE tb_channels VALIDATE CONSTRAINT tb_channels_tb_userboard_fk;
ALTER TABLE tb_widget VALIDATE CONSTRAINT newtable_tb_channels_fk;
ALTER TABLE tb_moduls VALIDATE CONSTRAINT tb_moduls_tb_widget_fk;
ALTER TABLE tb_user VALIDATE CONSTRAINT tb_user_tb_userdata_fk;
