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
	FAMILY "primary" (id_userdata, first_name, last_name, location, email)
);

CREATE TABLE tb_userboard (
	id_userboard INT NOT NULL DEFAULT unique_rowid(),
	id_userdata INT NULL,
	id_board INT NULL,
	CONSTRAINT tb_userboard_pk PRIMARY KEY (id_userboard ASC),
	CONSTRAINT tb_userboard_tb_board_fk FOREIGN KEY (id_board) REFERENCES tb_board (id_board) ON DELETE CASCADE ON UPDATE CASCADE,
	INDEX tb_userboard_auto_index_tb_userboard_tb_board_fk (id_board ASC),
	CONSTRAINT tb_userboard_tb_userdata_fk FOREIGN KEY (id_userdata) REFERENCES tb_userdata (id_userdata) ON DELETE CASCADE ON UPDATE CASCADE,
	INDEX tb_userboard_auto_index_tb_userboard_tb_userdata_fk (id_userdata ASC),
	FAMILY "primary" (id_userboard, id_userdata, id_board)
);

CREATE TABLE tb_channels (
	id_channels INT NOT NULL DEFAULT unique_rowid(),
	id_userboard INT NULL,
	nm_channels STRING NULL,
	channels_key STRING NULL,
	CONSTRAINT tb_channels_pk PRIMARY KEY (id_channels ASC),
	CONSTRAINT tb_channels_tb_userboard_fk FOREIGN KEY (id_userboard) REFERENCES tb_userboard (id_userboard) ON DELETE CASCADE ON UPDATE CASCADE,
	INDEX tb_channels_auto_index_tb_channels_tb_userboard_fk (id_userboard ASC),
	FAMILY "primary" (id_channels, id_userboard, nm_channels, channels_key)
);

CREATE TABLE tb_widget (
	id_widget INT NOT NULL DEFAULT unique_rowid(),
	nm_widget STRING NULL,
	CONSTRAINT tb_widget_pk PRIMARY KEY (id_widget ASC),
	FAMILY "primary" (id_widget, nm_widget)
);

CREATE TABLE tb_moduls (
	id_moduls INT NOT NULL DEFAULT unique_rowid(),
	id_channels INT NULL,
	id_widget INT NULL,
	nm_field STRING NULL,
	value_field STRING NULL,
	created_at TIMESTAMP WITH TIME ZONE NULL,
	CONSTRAINT tb_moduls_pk PRIMARY KEY (id_moduls ASC),
	CONSTRAINT tb_moduls_tb_widget_fk FOREIGN KEY (id_widget) REFERENCES tb_widget (id_widget) ON DELETE CASCADE ON UPDATE CASCADE,
	INDEX tb_moduls_auto_index_tb_moduls_tb_widget_fk (id_widget ASC),
	CONSTRAINT tb_moduls_tb_channels_fk FOREIGN KEY (id_channels) REFERENCES tb_channels (id_channels) ON DELETE CASCADE ON UPDATE CASCADE,
	INDEX tb_moduls_auto_index_tb_moduls_tb_channels_fk (id_channels ASC),
	FAMILY "primary" (id_moduls, id_channels, id_widget, nm_field, value_field, created_at)
);

CREATE TABLE tb_user (
	id_user INT NOT NULL DEFAULT unique_rowid(),
	id_userdata INT NULL,
	username STRING NULL,
	password STRING NULL,
	CONSTRAINT tb_user_pk PRIMARY KEY (id_user ASC),
	CONSTRAINT tb_user_tb_userdata_fk FOREIGN KEY (id_userdata) REFERENCES tb_userdata (id_userdata) ON DELETE CASCADE ON UPDATE CASCADE,
	INDEX tb_user_auto_index_tb_user_tb_userdata_fk (id_userdata ASC),
	FAMILY "primary" (id_user, id_userdata, username, password)
);
