import Search from "../../src/components/Search";
import { mount } from "cypress/react";
import { MemoryRouter } from "react-router-dom";

// Give component access to React Router
Cypress.Commands.add("mount", (component, options = {}) => {
  const { routerProps = { initialEntries: ["/"] }, ...mountOptions } = options;
  const wrapped = <MemoryRouter {...routerProps}>{component}</MemoryRouter>;
  return mount(wrapped, mountOptions);
});

describe("Search", () => {
  it("Rendered", () => {
    cy.mount(<Search />);
    cy.get("input");
  });
});
