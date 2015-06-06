--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: food_access; Type: TABLE; Schema: public; Owner: -; Tablespace:
--

CREATE TABLE food_access_triad (
    "CensusTract" text NOT NULL,
    "State" character varying(255) NOT NULL,
    "County" character varying(255) NOT NULL,
    "LILATracts_1And10" integer NOT NULL,
    "LILATracts_halfAnd10" integer NOT NULL,
    "LILATracts_1And20" integer NOT NULL,
    "LILATracts_Vehicle" integer NOT NULL,
    "Urban" integer NOT NULL,
    "Rural" integer NOT NULL,
    "LA1and10" integer NOT NULL,
    "LAhalfand10" integer NOT NULL,
    "LA1and20" integer NOT NULL,
    "LATracts_half" integer NOT NULL,
    "LATracts1" integer NOT NULL,
    "LATracts10" integer NOT NULL,
    "LATracts20" integer NOT NULL,
    "HUNVFlag" integer NOT NULL,
    "GroupQuartersFlag" integer NOT NULL,
    "OHU2010" integer NOT NULL,
    "NUMGQTRS" integer NOT NULL,
    "PCTGQTRS" real NOT NULL,
    "LowIncomeTracts" integer NOT NULL,
    "POP2010" integer NOT NULL,
    "UATYP10" character varying(255) NOT NULL,
    lapophalf real NOT NULL,
    lapophalfshare real NOT NULL,
    lalowihalf real NOT NULL,
    lalowihalfshare real NOT NULL,
    lakidshalf real NOT NULL,
    lakidshalfshare real NOT NULL,
    laseniorshalf real NOT NULL,
    laseniorshalfshare real NOT NULL,
    lahunvhalf real NOT NULL,
    lahunvhalfshare real NOT NULL,
    lapop1 real NOT NULL,
    lapop1share real NOT NULL,
    lalowi1 real NOT NULL,
    lalowi1share real NOT NULL,
    lakids1 real NOT NULL,
    lakids1share real NOT NULL,
    laseniors1 real NOT NULL,
    laseniors1share real NOT NULL,
    lahunv1 real NOT NULL,
    lahunv1share real NOT NULL,
    lapop10 real NOT NULL,
    lapop10share real NOT NULL,
    lalowi10 real NOT NULL,
    lalowi10share real NOT NULL,
    lakids10 real NOT NULL,
    lakids10share real NOT NULL,
    laseniors10 real NOT NULL,
    laseniors10share real NOT NULL,
    lahunv10 real NOT NULL,
    lahunv10share real NOT NULL,
    lapop20 real NOT NULL,
    lapop20share real NOT NULL,
    lalowi20 real NOT NULL,
    lalowi20share real NOT NULL,
    lakids20 real NOT NULL,
    lakids20share real NOT NULL,
    laseniors20 real NOT NULL,
    laseniors20share real NOT NULL,
    lahunv20 real NOT NULL,
    lahunv20share real NOT NULL
);


--
-- PostgreSQL database dump complete
--

