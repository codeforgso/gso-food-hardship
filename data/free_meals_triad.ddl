
CREATE TYPE day_of_week AS ENUM ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday');

CREATE TABLE free_meals_triad (
  day day_of_week,
  organization text,
  available_times text,
  address text,
  location geometry
);
