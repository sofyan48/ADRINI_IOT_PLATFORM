CREATE TABLE tb_board (
	id_board INT NOT NULL DEFAULT unique_rowid(),
	nm_board STRING NULL,
	serial_board STRING NULL,
	CONSTRAINT tb_board_pk PRIMARY KEY (id_board ASC),
	FAMILY "primary" (id_board, nm_board, serial_board)
);

CREATE TABLE tb_userdata (
	id_userdata INT NOT NULL DEFAULT unique_rowid(),
	email STRING NULL,
	access INT NOT NULL DEFAULT 1:::INT,
	CONSTRAINT tb_userdata_pk PRIMARY KEY (id_userdata ASC),
	UNIQUE INDEX tb_userdata_un (email ASC),
	FAMILY "primary" (id_userdata, email, access)
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

CREATE VIEW v_channels (id_channels, id_userboard, channels_key, nm_channels, id_board, nm_board, serial_board, id_userdata) AS SELECT m1.id_channels, m1.id_userboard, m1.channels_key, m1.nm_channels, m2.id_board, m3.nm_board, m3.serial_board, m2.id_userdata FROM iot_adrini.public.tb_channels AS m1 JOIN iot_adrini.public.tb_userboard AS m2 ON m1.id_userboard = m2.id_userboard JOIN iot_adrini.public.tb_board AS m3 ON m2.id_board = m3.id_board;

CREATE VIEW v_moduls (id_moduls, value_field, created_at, id_widget, nm_widget, id_channels, channels_key, nm_channels, id_board, id_userboard, id_userdata, nm_board, serial_board) AS SELECT m1.id_moduls, m1.value_field, m1.created_at, m1.id_widget, m2.nm_widget, m3.id_channels, m3.channels_key, m3.nm_channels, m4.id_board, m4.id_userboard, m4.id_userdata, m5.nm_board, m5.serial_board FROM iot_adrini.public.tb_moduls AS m1 JOIN iot_adrini.public.tb_widget AS m2 ON m1.id_widget = m2.id_widget JOIN iot_adrini.public.tb_channels AS m3 ON m2.id_channels = m3.id_channels JOIN iot_adrini.public.tb_userboard AS m4 ON m3.id_userboard = m4.id_userboard JOIN iot_adrini.public.tb_board AS m5 ON m4.id_board = m5.id_board;

CREATE VIEW v_userboard (id_board, id_userboard, id_userdata, nm_board, serial_board) AS SELECT m1.id_board, m1.id_userboard, m1.id_userdata, m2.nm_board, m2.serial_board FROM iot_adrini.public.tb_userboard AS m1 JOIN iot_adrini.public.tb_board AS m2 ON m1.id_board = m2.id_board;

CREATE VIEW v_widget (id_widget, id_channels, nm_widget, nm_channels, channels_key, id_userboard, id_userdata, id_board, email) AS SELECT a1.id_widget, a1.id_channels, a1.nm_widget, a2.nm_channels, a2.channels_key, a3.id_userboard, a3.id_userdata, a3.id_board, a4.email FROM iot_adrini.public.tb_widget AS a1 JOIN iot_adrini.public.tb_channels AS a2 ON a1.id_channels = a2.id_channels JOIN iot_adrini.public.tb_userboard AS a3 ON a2.id_userboard = a3.id_userboard JOIN iot_adrini.public.tb_userdata AS a4 ON a3.id_userdata = a4.id_userdata;

INSERT INTO tb_board (id_board, nm_board, serial_board) VALUES
	(428413380064182273, 'Adrini v1', 'ADR220219-001'),
	(429533030966951937, 'Adrini v1', 'ADR220219-001'),
	(429533227452039169, 'Adrini v1', 'ADR220219-001'),
	(429533483808489473, 'Adrini v1', 'ADR220219-001');

INSERT INTO tb_userdata (id_userdata, email, access) VALUES
	(428412005040783361, 'meongbego@gmail.com', 0);

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

ALTER TABLE tb_userboard ADD CONSTRAINT tb_userboard_tb_board_fk FOREIGN KEY (id_board) REFERENCES tb_board (id_board) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tb_userboard ADD CONSTRAINT tb_userboard_tb_userdata_fk FOREIGN KEY (id_userdata) REFERENCES tb_userdata (id_userdata) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tb_channels ADD CONSTRAINT tb_channels_tb_userboard_fk FOREIGN KEY (id_userboard) REFERENCES tb_userboard (id_userboard) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tb_widget ADD CONSTRAINT newtable_tb_channels_fk FOREIGN KEY (id_channels) REFERENCES tb_channels (id_channels) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tb_moduls ADD CONSTRAINT tb_moduls_tb_widget_fk FOREIGN KEY (id_widget) REFERENCES tb_widget (id_widget) ON DELETE CASCADE ON UPDATE CASCADE;

-- Validate foreign key constraints. These can fail if there was unvalidated data during the dump.
ALTER TABLE tb_userboard VALIDATE CONSTRAINT tb_userboard_tb_board_fk;
ALTER TABLE tb_userboard VALIDATE CONSTRAINT tb_userboard_tb_userdata_fk;
ALTER TABLE tb_channels VALIDATE CONSTRAINT tb_channels_tb_userboard_fk;
ALTER TABLE tb_widget VALIDATE CONSTRAINT newtable_tb_channels_fk;
ALTER TABLE tb_moduls VALIDATE CONSTRAINT tb_moduls_tb_widget_fk;
