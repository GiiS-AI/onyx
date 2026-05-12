import { cn } from "@opal/utils";

interface OnyxLogoTypedProps {
  size?: number;
  className?: string;
}

const SvgOnyxLogoTyped = ({ size: height, className }: OnyxLogoTypedProps) => {
  const h = height ?? 32;
  return (
    <div className={cn("flex flex-row items-center", className)}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src="/logotype.png" alt="GiiS" height={h} style={{ height: h, objectFit: "contain" }} className="dark:hidden" />
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src="/logotype-dark.png" alt="GiiS" height={h} style={{ height: h, objectFit: "contain" }} className="hidden dark:block" />
    </div>
  );
};
export default SvgOnyxLogoTyped;
