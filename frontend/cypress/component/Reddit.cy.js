import Reddit from "../../src/components/Reddit";
import { mount } from "cypress/react";
import { MemoryRouter } from "react-router-dom";

// Give component access to React Router
Cypress.Commands.add("mount", (component, options = {}) => {
  const { routerProps = { initialEntries: ["/"] }, ...mountOptions } = options;
  const wrapped = <MemoryRouter {...routerProps}>{component}</MemoryRouter>;
  return mount(wrapped, mountOptions);
});

describe("Reddit", () => {
  it("Rendered", () => {
    cy.mount(<Reddit />);
    cy.get("div").should("have.class", "reddit-box-body");
  });
});
