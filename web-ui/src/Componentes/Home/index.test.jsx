import React from "react";
import { screen, render } from "@testing-library/react";
import { BrowserRouter  } from "react-router-dom";

import Home from './';

beforeEach(() => render(<BrowserRouter ><Home/></BrowserRouter>));
describe("Home",() => {

  it("gitpython", () => {
    expect(screen.queryByText(/gitpython/i)).toBeInTheDocument();
  });

  it("prs", () => {
    expect(screen.queryByText(/prs/i)).toBeInTheDocument();
  });

  it("ramas", () => {
    expect(screen.queryByText(/ramas/i)).toBeInTheDocument();
  });

});