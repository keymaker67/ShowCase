import { useAccordionButton } from "react-bootstrap/AccordionButton";
import Button from "react-bootstrap/Button";

const useCustomToggle = ({ children, eventKey }) => {
  const decoratedOnClick = useAccordionButton(eventKey);
  return (
    <Button
      href="#letsPracticeMore"
      variant="primary"
      onClick={decoratedOnClick}
    >
      {children}
    </Button>
  );
};

export default useCustomToggle;
