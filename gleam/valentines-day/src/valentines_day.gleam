pub type Approval {
  Yes
  No
  Maybe
}

pub type Cuisine {
  Korean
  Turkish
}

pub type Genre {
  Crime
  Horror
  Romance
  Thriller
}

pub type Activity {
  BoardGame
  Chill
  Movie(Genre)
  Restaurant(Cuisine)
  Walk(Int)
}

pub fn rate_activity(activity: Activity) -> Approval {
  case activity {
    Movie(genre) if genre == Romance -> Yes
    Restaurant(cuisine) if cuisine == Korean -> Yes
    Restaurant(cuisine) if cuisine == Turkish -> Maybe
    Walk(n) if n > 11 -> Yes
    Walk(n) if n > 6 -> Maybe
    _ -> No
  }
}
