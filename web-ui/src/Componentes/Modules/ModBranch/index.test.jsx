import React from "react";
import { screen, render } from "@testing-library/react";
import { BrowserRouter  } from "react-router-dom";

import ModPRs from './';

beforeEach(() => render(<BrowserRouter ><ModPRs/></BrowserRouter>));
describe("ModPRs",() => {

  it("branch", () => {
    expect(screen.queryByText(/branch/i)).toBeInTheDocument();
  });

  it("volver", () => {
    expect(screen.getByText(/volver/i)).toBeInTheDocument();
  });
});