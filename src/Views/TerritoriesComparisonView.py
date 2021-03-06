from sqlalchemy.orm.exc import NoResultFound

from src.Views.Exceptions.EmptyTerritoryException import EmptyTerritoryException
from src.Views.Exceptions.EmptyYearException import EmptyYearException
from src.Views.Utils import select_territory, get_percentage_of_people_that_passed


def territories_comparison_view(active_filter):
    try:
        territory1 = select_territory()
        if territory1 is not None:
            territory2 = select_territory()
            if territory2 is not None:
                years1 = territory1.years
                years2 = territory2.years
                if len(years1) == 0 or len(years2) == 0:
                    raise EmptyTerritoryException
                for i in range(len(years1)):
                    score1 = get_percentage_of_people_that_passed(years1[i], active_filter)
                    score2 = get_percentage_of_people_that_passed(years2[i], active_filter)
                    better_territory = territory1.name if score1 > score2 else territory2.name
                    print("%d - %s" % (years1[i].year_number, better_territory))
    except NoResultFound:
        print("There are no territories in database")
    except EmptyTerritoryException:
        print("Territory has no years")
    except EmptyYearException:
        print("Year has no attendants")
