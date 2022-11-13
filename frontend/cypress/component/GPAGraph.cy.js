import GPAGraph from "../../src/components/GPAGraph";
import { mount } from "cypress/react";
import { MemoryRouter } from "react-router-dom";

// Give component access to React Router
Cypress.Commands.add("mount", (component, options = {}) => {
  const { routerProps = { initialEntries: ["/"] }, ...mountOptions } = options;
  const wrapped = <MemoryRouter {...routerProps}>{component}</MemoryRouter>;
  return mount(wrapped, mountOptions);
});

describe("GPAGraph", () => {
  it("Rendered", () => {
    cy.mount(<GPAGraph />);
    cy.get("div").should("have.class", "recharts-wrapper");
  });
});
