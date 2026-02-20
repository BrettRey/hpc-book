# Varieties as conditioning structure (draft notes for Ch15)

## Core proposal
- Register, dialect, and discourse community are not distinct ontological types. They are different conditioning structures in a probabilistic model of production.
- The key question is not "who/where" but "what variable do you condition on" when predicting form choices and how stable that variable is.

## Three-way distinction (conditioning variables)
1. **Discourse community** = latent mixture component over input sources.
   - Learners infer clusters of sources with distinct distributions.
   - Community membership is a latent variable; it shapes expectations of what counts as normal.
2. **Register** = situational conditioning within a repertoire.
   - Context (activity type, medium, stance) reweights construction choice probabilities.
   - Register does not change the opportunity set; it changes rates.
3. **Dialect** = durable population-level parameterization across contexts.
   - A persistent baseline tied to speaker/network; survives across registers.
   - Dialect shifts are broad and stable, not tied to a single situational cue.

## Bayesian framing
- Constructional choice modeled as conditional probability: P(Y | R, S, ...)
- Register: P(Y | R=r) with parameters theta_r.
- Dialect: P(Y | dialect d, register r) with additive or hierarchical effects.
- Discourse community: latent mixture C with its own parameters; speakers draw from components.
- Indexical meaning = inverse conditioning: if Y depends on X, then Y provides evidence about X.

## Standardization as hyper-prior precision
- Standard varieties modeled as high-precision priors with low variance.
- Standardization can mask dialect differences in certain registers (e.g., formal writing), while spoken registers allow dialectal effects to surface.

## Normativity reinterpreted
- "Unacceptability" corresponds to low posterior predictive probability under the distribution relevant to the listener's conditioning structure.
- This yields gradient, context-sensitive normativity without prescriptive obligations.

## Extensions / variants
- Style-shifting: speakers can draw from multiple community components (mixture weights).
- Community boundaries are not fixed; latent mixture components can be inferred from data.
- Identifiability and confounding issues highlight need for rich metadata and cross-classified data.

## Relevance to Ch15
- Provides the chapter's technical spine for dialect/register/discourse community distinctions.
- Connects naturally to HPC: stable clusters maintained by repeated conditioning and reinforcement.
- Supports the communicative situation framing: register is the linguistic face of com-sits; discourse communities are latent population structures; dialect is durable parameterization.
- Offers a formal way to talk about "native speaker" and standardization as hyper-parameters rather than categorical essences.

## Drafting hooks
- "Varieties differ by conditioning structure, not by ontological type."  
- "Register is situational conditioning; dialect is durable parameterization; discourse community is a latent mixture component."  
- "Indexical meaning is just inverse conditioning."  

## Cautions
- Keep the Bayesian framing as an explanatory idealization, not a literal cognitive claim.
- Emphasize that the framework is about rates and distributions, not categorical rule changes.


## Additional details
- The model frames linguistic choices as draws from distributions over competing constructions within an "opportunity set" (a constructional niche).
- Dialect effects are modeled as speaker-level parameters that persist across registers; register effects are context-level parameters that shift within the same speaker.
- Discourse community is modeled as a latent mixture; speakers can have mixture weights (style-shifting), allowing partial membership and dynamic identity performance.
- The framework predicts that indexical meaning is emergent: once a form is conditioned on a variable (dialect, register, community), observing the form provides evidence about that variable.
- Standardization is treated as a high-precision prior that reduces variability; formal writing can suppress dialectal variance for morphosyntax while leaving phonology to spoken contexts.

## Extra Ch15 leverage
- This framework can provide the chapter's backbone for organizing dialect/register/community into a single conceptual architecture.
- It lets you talk about "native speaker" as an inference about mixture weights and exposure history rather than a categorical essence.
- It helps justify why linguistic norms are gradient and context-sensitive: probability distributions, not categorical rule-switching.


## Empirical diagnostics implied by the framework
- If register is a situational conditioning variable, you should observe the same speaker shifting probabilities across contexts while maintaining the same baseline dialect effects.
- If dialect is a durable parameterization, you should observe stable shifts across multiple registers for the same speakers or networks.
- If discourse community is a latent mixture, you should see clustering in distributions that is not fully explained by register or dialect; membership should predict norms and acceptability judgments.

## Extra Ch15 leverage
- These diagnostics can become a "methods" paragraph: what kinds of data would falsify the conditioning-structure account (e.g., no stable shifts across registers, no mixture structure, no indexical inference effects).
- Gives a way to talk about "native speaker" as a probabilistic inference problem: how much exposure and how many contexts are needed to shift the posterior.

