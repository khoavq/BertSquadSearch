import React from 'react';
import { Dimmer, Loader } from 'semantic-ui-react';

const LoadingComponent = ({
  inverted = true,
  content
}) => {
  return (
    <Dimmer active inverted={inverted}>
      <Loader content={content} size={"massive"}/>
    </Dimmer>
  );
};

export default LoadingComponent;
