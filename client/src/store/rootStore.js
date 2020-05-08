import { createContext } from "react";
import { action, observable } from "mobx";

export class RootStore {
  @observable qnaResult = {};
  @action setQnAResult = hits => (this.qnaResult = hits);
}

export const RootStoreContext = createContext(new RootStore());
