import React, { useContext, useState } from "react";
import { Menu, MenuItem, Input, Button, Select } from "semantic-ui-react";
import Axios from "axios";
import { RootStoreContext } from "../store/rootStore";
import _ from "lodash";

const Navbar = () => {
  const rootStore = useContext(RootStoreContext);
  let { searchOption, setSearchOption } = rootStore;
  let [query, setQuery] = useState("");

  const handleOnClick = async () => {
    rootStore.loading.set(true);
    const res = await Axios.get(
      `http://localhost:5000/qna?q=${query}&limit=${searchOption}`
    );
    rootStore.loading.set(false);
    rootStore.setQnAResult(res.data);
    console.log(res.data);
  };

  const searchOptions = [
    { key: 1, value: 1, text: "1 result" },
    { key: 2, value: 2, text: "2 results" },
    { key: 3, value: 5, text: "5 results" },
    { key: 4, value: 10, text: "10 results" },
  ];

  return (
    <Menu fixed="top" color="blue" widths={2} fluid inverted>
      <MenuItem>
        <Input
          action
          fluid
          placeholder="Enter your question..."
          onChange={(e) => setQuery(e.target.value)}
        >
          <input />
          <Select
            compact
            options={searchOptions}
            defaultValue={searchOption}
            onChange={(e, { value }) => setSearchOption(value)}
          />
          <Button content="Search" color="teal" onClick={handleOnClick} />
        </Input>
      </MenuItem>
    </Menu>
  );
};

export default Navbar;
