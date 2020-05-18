import React, { useContext, Fragment } from "react";
import { Segment, Grid, GridColumn } from "semantic-ui-react";
import { RootStoreContext } from "../store/rootStore";
import { observer } from "mobx-react-lite";
import LoadingComponent from "./LoadingComponent";

const colors = ["orange", "teal", "purple"];
const randomColor = (index) => {
  return colors[index];
};

const ResultList = () => {
  const rootStore = useContext(RootStoreContext);
  const { qnaResult, loading } = rootStore;

  const getHighlightedText = (text, highlight) => {
    const parts = text.split(new RegExp(`(${highlight})`, "gi"));
    return (
      <span>
        {" "}
        {parts.map((part, i) => (
          <span
            key={i}
            style={
              part.toLowerCase() === highlight.toLowerCase()
                ? { fontWeight: "bold", background: "yellow" }
                : {}
            }
          >
            {part}
          </span>
        ))}{" "}
      </span>
    );
  };

  const mapResultToComponents = (result, index) =>
    result.context && (
      <Segment size="big" key={index} color={randomColor(index)}>
        <p>
          <strong>Paragraph:</strong>{" "}
          {getHighlightedText(result.context, result.answer)}
        </p>
        <p>
          <strong>Answer:</strong> {result.answer}
        </p>
      </Segment>
    );

  return (
    <Fragment>
      {loading.get() ? (
        <LoadingComponent content={"Searching..."} />
      ) : (
        <Grid className="container">
          <GridColumn>
            {qnaResult.length > 0 &&
              qnaResult.map((result, index) =>
                mapResultToComponents(result, index)
              )}
          </GridColumn>
        </Grid>
      )}
    </Fragment>
  );
};

export default observer(ResultList);
