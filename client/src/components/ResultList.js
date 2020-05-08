import React, { useContext } from "react";
import { Segment, Grid, GridColumn } from "semantic-ui-react";
import { RootStoreContext } from "../store/rootStore";
import { observer } from "mobx-react-lite";

const ResultList = () => {
  const rootStore = useContext(RootStoreContext);
  const { qnaResult } = rootStore;

  const getHighlightedText = (text, highlight) => {
    const parts = text.split(new RegExp(`(${highlight})`, 'gi'));
    return <span> { parts.map((part, i) =>
        <span key={i} style={part.toLowerCase() === highlight.toLowerCase() ? { fontWeight: 'bold', background: "yellow" } : {} }>
            { part }
        </span>)
    } </span>;
}

  const mapResultToComponents = (result) => (
      result.context && (
      <Segment size="big">
        <p>
          <strong>Paragraph:</strong>{" "}
          {getHighlightedText(result.context, result.answer)}
        </p>
        <p>
          <strong>Anwser:</strong>{" "}
          {result.answer}
        </p>
      </Segment>
    ))

  return (
    <Grid className="container">
      <GridColumn>
        {mapResultToComponents(qnaResult)}
      </GridColumn>

    </Grid>
  );
};

export default observer(ResultList);
