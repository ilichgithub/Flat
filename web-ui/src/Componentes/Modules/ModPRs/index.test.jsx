import React from "react";
import { screen, render } from "@testing-library/react";
import { BrowserRouter  } from "react-router-dom";

import ModPRs from './';

beforeEach(() => render(<BrowserRouter ><ModPRs/></BrowserRouter>));
describe("ModPRs",() => {

  it("prs", () => {
    expect(screen.queryByText(/prs/i)).toBeInTheDocument();
  });
  it("volver", () => {
    expect(screen.queryByText(/volver/i)).toBeInTheDocument();
  });
  it("agregar", () => {
    expect(screen.queryByText(/agregar/i)).toBeInTheDocument();
  });
  it("origen", () => {
    expect(screen.queryByText(/volver/i)).toBeInTheDocument();
  });
  it("destino", () => {
    expect(screen.queryByText(/volver/i)).toBeInTheDocument();
  });
});