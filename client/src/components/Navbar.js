import React, {useContext} from "react";
import {Menu, MenuItem, Input} from "semantic-ui-react";
import Axios from "axios";
import {RootStoreContext} from "../store/rootStore";
import _ from "lodash";

const Navbar = props => {
    const rootStore = useContext(RootStoreContext);

    const handleOnChange = _.debounce(async query => {
        if (query.length < 4) {
            return;
        }
        const res = await Axios.get(`http://localhost:5000/qna?q=${query}`);
        console.log(res.data)
        rootStore.setQnAResult(res.data)
    }, 500);

    return (
        <Menu fixed="top" color="blue" inverted widths={3}>
            <MenuItem>
                <Input
                    fluid
                    className="icon"
                    icon="search"
                    placeholder="Search..."
                    onChange={e => handleOnChange(e.target.value)}
                />
            </MenuItem>
        </Menu>
    );
};

export default Navbar;
