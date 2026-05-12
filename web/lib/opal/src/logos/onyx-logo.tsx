import type { IconProps } from "@opal/types";
const SvgOnyxLogo = ({ size, className }: IconProps) => (
  <span className={className} style={{ display: "inline-flex", flexShrink: 0 }}>
    {/* eslint-disable-next-line @next/next/no-img-element */}
    <img src="/logo.png" alt="GiiS" height={size} width={size} style={{ height: size, width: size, objectFit: "contain" }} className="dark:hidden" />
    {/* eslint-disable-next-line @next/next/no-img-element */}
    <img src="/logo-dark.png" alt="GiiS" height={size} width={size} style={{ height: size, width: size, objectFit: "contain" }} className="hidden dark:block" />
  </span>
);
export default SvgOnyxLogo;
