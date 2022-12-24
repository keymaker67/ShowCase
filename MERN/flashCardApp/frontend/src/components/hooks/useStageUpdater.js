import axios from "axios";
import { useEffect, useState } from "react";

export default function useStageUpdater(url) {
  const [loading, setLoading] = useState(false);
  const [flashCards, setFlashCards] = useState([]);

  useEffect(() => {
    const flashCardsUpdater = async () => {
      setLoading(true);

      const today = new Date().getTime();
      const res = await axios.get(url);
      const flashCards = res.data.words;

      // eslint-disable-next-line array-callback-return
      flashCards.map((flashCard) => {
        const dayDifference = Math.floor(
          (today - flashCard.last_review_date) / (24 * 60 * 60 * 1000)
        );
        switch (flashCard.stage) {
          case 0:
            if (dayDifference > 0)
              setFlashCards((perv) => [...perv, flashCard]);
            break;
          case 1:
            if (dayDifference > 0)
              setFlashCards((perv) => [...perv, flashCard]);
            break;
          case 2:
            if (dayDifference > 0)
              setFlashCards((perv) => [...perv, flashCard]);
            break;
          case 3:
            if (dayDifference > 3)
              setFlashCards((perv) => [...perv, flashCard]);
            break;
          case 4:
            if (dayDifference > 7)
              setFlashCards((perv) => [...perv, flashCard]);
            break;
          case 5:
            if (dayDifference > 14)
              setFlashCards((perv) => [...perv, flashCard]);
            break;
          default:
            break;
        }
      });
      setLoading(false);
    };
    flashCardsUpdater();
  }, []);

  return { flashCards, loading };
}
