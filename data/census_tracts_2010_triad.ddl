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
-- Name: census_tracts_2010; Type: TABLE; Schema: public; Owner: -; Tablespace:
--

CREATE TABLE census_tracts_2010_triad (
    ogc_fid integer NOT NULL,
    wkb_geometry geometry(MultiPolygonZ,4269),
    statefp10 character varying(2),
    countyfp10 character varying(3),
    tractce10 character varying(6),
    geoid10 character varying(11),
    name10 character varying(7),
    namelsad10 character varying(20),
    mtfcc10 character varying(5),
    funcstat10 character varying(1),
    aland10 double precision,
    awater10 double precision,
    intptlat10 character varying(11),
    intptlon10 character varying(12)
);


--
-- Name: census_tracts_2010_ogc_fid_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE census_tracts_2010_ogc_fid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: census_tracts_2010_ogc_fid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE census_tracts_2010_ogc_fid_seq OWNED BY census_tracts_2010_triad.ogc_fid;


--
-- Name: ogc_fid; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY census_tracts_2010_triad ALTER COLUMN ogc_fid SET DEFAULT nextval('census_tracts_2010_ogc_fid_seq'::regclass);


--
-- Name: census_tracts_2010_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace:
--

ALTER TABLE ONLY census_tracts_2010_triad
    ADD CONSTRAINT census_tracts_2010_pkey PRIMARY KEY (ogc_fid);


--
-- Name: census_tracts_2010_wkb_geometry_geom_idx; Type: INDEX; Schema: public; Owner: -; Tablespace:
--

CREATE INDEX census_tracts_2010_wkb_geometry_geom_idx ON census_tracts_2010_triad USING gist (wkb_geometry);


--
-- PostgreSQL database dump complete
--

